
````markdown
# 📄 txt_to_pdf_with_watermark

这是一个将 `.txt` 文本文件转换为 PDF 文件的小工具，支持中文显示，并可添加自定义水印。适合用于生成中文文档、报告、公告等。

---

## ✨ 功能介绍

- ✅ 支持从命令行运行，快速生成 PDF
- ✅ 支持中文内容，无乱码
- ✅ 自动添加对角线水印
- ✅ 可自定义水印内容
- ✅ 默认输出与输入文件同名的 PDF 文件

---

## ⚙️ 安装依赖

请确保安装了 Python 环境（建议 Python 3.7+），然后使用以下命令安装必要的库：

```bash
pip install reportlab
````

---

## 🖥️ 使用方法

```bash
python txt_to_pdf_with_watermark.py 输入文件路径.txt "水印文字"
```

### 示例：

```bash
python txt_to_pdf_with_watermark.py example.txt "保密文件"
```

若不填写水印文字，默认使用 `"机密"` 作为水印：

```bash
python txt_to_pdf_with_watermark.py example.txt
```

输出文件将为 `example.pdf`，保存在当前目录中。

---

## 📄 示例输入 & 输出

**输入文件 `example.txt`：**

```
这是一个测试文档。
支持中文内容和多段文字。

输出为 PDF，并添加水印。
```

**输出文件 `example.pdf`：**

* 内容为输入文本格式
* 每页中央对角线有“保密文件”水印
* 使用支持中文的字体
* 标准 A4 页面、默认边距

---

## 🧩 如何修改默认格式

你可以在 `txt_to_pdf_with_watermark.py` 文件中修改以下部分，定制格式：

### 1. 设置页边距（单位：毫米）

```python
margins=(25, 25, 25, 25)  # 左、右、上、下边距
```

### 2. 修改字体大小

```python
font_size=12  # 例如改成14会更大
```

### 3. 更改字体（已默认支持中文）

```python
font_name='HeiseiMin-W3'  # 可选中文字体: HeiseiKakuGo-W5（更粗）、HeiseiMin-W3（更细）
```

### 4. 调整水印样式

你可以在函数 `add_watermark()` 中修改透明度、字体大小、颜色等：

```python
canvas.setFont(font_name, 50)               # 字体大小
canvas.setFillColorRGB(0.9, 0.9, 0.9)        # 水印颜色（越接近1越淡）
canvas.rotate(45)                            # 旋转角度
```

---

## 📬 联系方式 & 贡献

欢迎反馈问题或提建议，欢迎自行 Fork 后扩展功能（如分页、页码、加密等）。

```
