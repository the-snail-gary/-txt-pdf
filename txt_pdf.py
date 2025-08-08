import argparse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


def txt_to_pdf_with_watermark(
    txt_path,
    pdf_path='output.pdf',
    watermark_text='机密',
    font_name='HeiseiMin-W3',
    font_size=12,
    margins=(25, 25, 25, 25)
):
    # 注册支持中文的字体
    pdfmetrics.registerFont(UnicodeCIDFont(font_name))

    # 页面设置
    page_width, page_height = A4
    left_margin, right_margin, top_margin, bottom_margin = [m * mm for m in margins]

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin
    )

    # 样式设置
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Chinese',
        fontName=font_name,
        fontSize=font_size,
        leading=font_size * 1.5
    ))

    # 读取txt内容
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 转换为段落
    story = []
    for line in lines:
        line = line.strip()
        if line:
            story.append(Paragraph(line, styles['Chinese']))
            story.append(Spacer(1, 6))

    # 添加水印函数
    def add_watermark(canvas, doc):
        canvas.saveState()
        canvas.setFont(font_name, 50)
        canvas.setFillColorRGB(0.9, 0.9, 0.9)
        canvas.translate(page_width / 2, page_height / 2)
        canvas.rotate(45)
        canvas.drawCentredString(0, 0, watermark_text)
        canvas.restoreState()

    # 构建PDF
    doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)
    print(f"✅ PDF生成成功：{pdf_path}")


# 添加命令行支持
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='将TXT文件转换为带中文水印的PDF文件')
    parser.add_argument('txt_path', help='输入的TXT文件路径')
    parser.add_argument('watermark', nargs='?', default='机密', help='水印文字（默认：机密）')
    args = parser.parse_args()

    output_pdf = args.txt_path.rsplit('.', 1)[0] + '.pdf'
    txt_to_pdf_with_watermark(
        txt_path=args.txt_path,
        pdf_path=output_pdf,
        watermark_text=args.watermark
    )
