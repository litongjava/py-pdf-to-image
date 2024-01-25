import fitz  # PyMuPDF
import os


def pdf_to_images(pdf_path, output_dir='.'):
  # 打开 PDF 文件
  doc = fitz.open(pdf_path)

  # 获取不带路径的 PDF 文件名（不含扩展名）
  pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

  # 遍历每一页
  for page_num in range(len(doc)):
    # 获取页面
    page = doc.load_page(page_num)

    # 将页面渲染为图像（pix）
    pix = page.get_pixmap()

    # 定义图像的输出路径
    image_path = os.path.join(output_dir, f"{pdf_name}_{page_num + 1}.png")

    # 将图像保存到文件
    pix.save(image_path)

    print(f"Image saved: {image_path}")

  # 关闭文档
  doc.close()


if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Convert PDF to images.')
  parser.add_argument('pdf_path', type=str, help='Path to the input PDF file.')
  parser.add_argument('-d', '--output_dir', type=str, default='.', help='Directory to save output images.')

  args = parser.parse_args()

  # 确保输出目录存在
  if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

  pdf_to_images(args.pdf_path, args.output_dir)
