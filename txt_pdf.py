import argparse
import random
import string
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
import pikepdf
import os


def generate_random_noise(length=500):
    chars = string.ascii_letters + string.digits + '的一是在不了有和人这中大为上个国我以要他时来用们生到作地于出就分对成会可主发年动同工也能下过子说产种面而方后多定行学法所民得经十三之进着等部度家电力里如水化高自二理起小物现实加量都两体制机当使点从业本去把性好应开它合还因由其些然前外天政四日那社义事平形相全表间样与关各重新线内数正心反你明看原又么利比或但质气第向道命此变条只没结解问意建月公无系军很情者最立代想已通并提直题党程展五果料象员革位入常文总次品式活设及管特件长求老头基资边流路级少图山统接知较将组见计别她手角期根论运农指几九区强放决西被干做必战先回则任取据处理府研质信四海'''

    return ''.join(random.choices(chars, k=length))


def txt_to_pdf_with_watermark(
    txt_path,
    pdf_path='output.pdf',
    watermark_text='机密',
    font_name='HeiseiMin-W3',
    font_size=12,
    margins=(25, 25, 25, 25),
    add_noise=True
):
    # 注册中文字体
    pdfmetrics.registerFont(UnicodeCIDFont(font_name))

    # 页面与边距
    page_width, page_height = A4
    left_margin, right_margin, top_margin, bottom_margin = [m * mm for m in margins]

    # 样式
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Chinese',
        fontName=font_name,
        fontSize=font_size,
        leading=font_size * 1.5
    ))

    # 读取txt文件
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 处理文本为段落
    story = []
    for line in lines:
        line = line.strip()
        if line:
            story.append(Paragraph(line, styles['Chinese']))
            story.append(Spacer(1, 6))

    # 水印 + 边缘乱码函数
    def add_watermark(canvas, doc):
        canvas.saveState()

        # 正中水印
        canvas.setFont(font_name, 50)
        canvas.setFillColorRGB(0.9, 0.9, 0.9)
        canvas.translate(page_width / 2, page_height / 2)
        canvas.rotate(45)
        canvas.drawCentredString(0, 0, watermark_text)
        canvas.restoreState()

        # 添加左右两侧的竖排乱码
        if add_noise:
            canvas.saveState()
            canvas.setFont(font_name, 8)
            canvas.setFillColorRGB(0.7, 0.7, 0.7)

            noise = generate_random_noise(120)  # 竖排字符数，控制页面高度
            vertical_spacing = 10  # 间距（单位：pt）

            # 左侧竖排乱码，从顶部往下
            x_left = 10 * mm
            y_top = page_height - 40 * mm
            for i, char in enumerate(noise):
                y = y_top - i * vertical_spacing
                if y < 30 * mm:
                    break
                canvas.saveState()
                canvas.translate(x_left, y)
                canvas.rotate(90)  # 旋转90度，使文字竖立
                canvas.drawString(0, 0, char)
                canvas.restoreState()

            # 右侧竖排乱码
            x_right = page_width - 10 * mm
            for i, char in enumerate(noise):
                y = y_top - i * vertical_spacing
                if y < 30 * mm:
                    break
                canvas.saveState()
                canvas.translate(x_right, y)
                canvas.rotate(90)
                canvas.drawString(0, 0, char)
                canvas.restoreState()

            canvas.restoreState()



    # 生成PDF
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin
    )
    doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)
    print(f"✅ PDF生成成功：{pdf_path}")


def encrypt_pdf_in_place(input_path, password):
    temp_path = input_path + '.tmp.pdf'
    pdf = pikepdf.open(input_path)
    pdf.save(temp_path, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
    os.remove(input_path)
    os.rename(temp_path, input_path)
    print(f"🔐 已加密：{input_path}，打开需密码：{password}")


# 命令行入口
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='将TXT转换为带水印和乱码干扰的PDF，可选加密')
    parser.add_argument('txt_path', help='输入的TXT文件路径')
    parser.add_argument('watermark', nargs='?', default='机密', help='水印文字（默认：机密）')
    parser.add_argument('--password', help='设置PDF打开密码（可选）')
    parser.add_argument('--no-noise', action='store_true', help='不添加边缘乱码')

    args = parser.parse_args()
    output_pdf = args.txt_path.rsplit('.', 1)[0] + '.pdf'

    txt_to_pdf_with_watermark(
        txt_path=args.txt_path,
        pdf_path=output_pdf,
        watermark_text=args.watermark,
        add_noise=not args.no_noise
    )

    if args.password:
        encrypt_pdf_in_place(output_pdf, args.password)
