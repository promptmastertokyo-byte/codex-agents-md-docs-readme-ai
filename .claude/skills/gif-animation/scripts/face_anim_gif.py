#!/usr/bin/env python3
"""2枚のキーフレーム画像から、指定領域だけをアニメーションさせるループGIFを生成する。

フレームA(始点)を全面のベースとして固定し、指定した楕円領域内だけを
フレームB(終点)へブレンドして戻す。領域外は1ピクセルも動かないため、
紙テクスチャや背景のチラつき・画面全体の揺れが起きない。

使用例:
    python3 face_anim_gif.py frameA.png frameB.png out.gif \
        --region 795,330,155,135 --hold-a 2000 --hold-b 3000

--region は元画像座標での楕円 cx,cy,rx,ry。複数指定可。
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFilter


def parse_region(text):
    parts = [float(v) for v in text.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("region は cx,cy,rx,ry の4値")
    return parts


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("frame_a", help="始点フレーム(ベースとして全面固定)")
    p.add_argument("frame_b", help="終点フレーム(領域内のみ使用)")
    p.add_argument("out", help="出力GIFパス")
    p.add_argument("--region", type=parse_region, action="append", required=True,
                   help="アニメーションさせる楕円 cx,cy,rx,ry(元画像座標・複数可)")
    p.add_argument("--hold-a", type=int, default=2000, help="A表示ms(既定2000)")
    p.add_argument("--hold-b", type=int, default=3000, help="B表示ms(既定3000)")
    p.add_argument("--trans-ms", type=int, default=65,
                   help="遷移1フレームあたりms(既定65)")
    p.add_argument("--width", type=int, default=720, help="出力幅px(既定720)")
    p.add_argument("--mask-blur", type=int, default=14,
                   help="マスク境界のぼかし半径(既定14)")
    args = p.parse_args()

    a = Image.open(args.frame_a).convert("RGB")
    b = Image.open(args.frame_b).convert("RGB")
    if a.size != b.size:
        raise SystemExit(f"サイズ不一致: {a.size} vs {b.size}")
    scale = args.width / a.width
    size = (args.width, round(a.height * scale))
    a = a.resize(size, Image.LANCZOS)
    b = b.resize(size, Image.LANCZOS)

    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    for cx, cy, rx, ry in args.region:
        d.ellipse((round((cx - rx) * scale), round((cy - ry) * scale),
                   round((cx + rx) * scale), round((cy + ry) * scale)), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(args.mask_blur))

    def blend(t):
        if t <= 0:
            return a.copy()
        m = mask.point(lambda v: round(v * t))
        out = a.copy()
        out.paste(b, (0, 0), m)
        return out

    frames, durations = [], []

    def add(img, ms):
        frames.append(img)
        durations.append(ms)

    add(a, args.hold_a)
    for t in (0.35, 0.7):                 # A→B イーズイン
        add(blend(t), args.trans_ms)
    add(blend(1.0), args.hold_b)
    for t in (0.7, 0.35):                 # B→A イーズアウト
        add(blend(t), args.trans_ms)

    # 共通パレット・ディザ無しで量子化(パステル調でもバンディングが出にくく軽い)
    pal = frames[0].quantize(colors=256, method=Image.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    q[0].save(args.out, save_all=True, append_images=q[1:],
              duration=durations, loop=0, optimize=True)
    print(f"{args.out}: {os.path.getsize(args.out) / 1e6:.2f} MB, "
          f"{len(frames)} frames")


if __name__ == "__main__":
    main()
