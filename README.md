
````markdown
# 📄 txt_to_pdf_with_watermark

将 `.txt` 文本文件转换为 PDF，支持：

- ✅ 中文段落渲染
- ✅ 中心斜向水印文字
- ✅ 左右页边添加竖排乱码（扰乱 OCR/AI）
- ✅ PDF 密码保护（选填）

---

## ✨ 功能介绍

- 📄 将纯文本 `.txt` 转为格式化 PDF
- 🌐 中文支持，避免乱码
- 🔐 可设置打开密码，加密 PDF（不会保留未加密副本）
- 📶 可在页面左右边距添加竖排乱码，增强反爬保护
- 🖨️ 支持命令行调用

---

## ⚙️ 安装依赖

请确保安装 Python（建议 3.7+），然后运行：

```bash
pip install reportlab pikepdf
````

---

## 🖥️ 使用方法

```bash
python txt_to_pdf_with_watermark.py 输入文件.txt "水印文字" [--password 密码] [--no-noise]
```

### 示例：

```bash
# 生成 PDF，添加“保密文件”水印、竖排乱码、设置密码123456
python txt_to_pdf_with_watermark.py example.txt "保密文件" --password 123456

# 默认水印“机密”，添加乱码，但不设置密码
python txt_to_pdf_with_watermark.py example.txt

# 添加水印，但不插入乱码干扰
python txt_to_pdf_with_watermark.py example.txt "内部资料" --no-noise
```

---

## 📄 示例输入输出

**输入文件 `example.txt`：**

```
这是一个测试文档。
支持中文内容和多段文字。

输出为 PDF，并添加水印。
```

**输出 PDF 特征：**

* 页眉居中添加斜向水印（例如“保密文件”）
* 页面左/右边距竖排乱码干扰字符（默认开启）
* 可设置 PDF 打开密码（选填）

---

## 🧩 可自定义格式（可在代码中修改）

| 参数   | 位置                           | 说明                |
| ---- | ---------------------------- | ----------------- |
| 字体大小 | `font_size=12`               | 调整正文字体大小          |
| 页边距  | `margins=(25,25,25,25)`      | 单位为 mm            |
| 水印样式 | `setFont(...), rotate(...)`  | 可调整水印字体大小、透明度等    |
| 乱码长度 | `generate_random_noise(120)` | 每页竖排乱码字符数量        |
| 乱码间距 | `vertical_spacing=10`        | 两字符之间的竖向间距（单位 pt） |

---

## 📬 常见问题

### ❓ 乱码太显眼怎么办？

可以调低字体大小和颜色透明度，例如：

```python
canvas.setFont(font_name, 6)
canvas.setFillColorRGB(0.85, 0.85, 0.85)
```

### ❓ 水印太重影响阅读？

将 `setFillColorRGB(0.9, 0.9, 0.9)` 改为 `(0.95, 0.95, 0.95)` 即更淡。

---

## 🧪 TODO（欢迎 PR）

* [ ] 支持分页页码
* [ ] 导入 Word 或 HTML 源文件
* [ ] 自定义输出路径或文件名

---

## 📎 联系方式 & 贡献

如需功能增强或样式定制，欢迎提交 Issue 或 PR。

```

---

是否需要我也一并更新 `.py` 文件的顶部注释为中文？或者将整个项目结构打包给你下载（zip / Git repo）？你说一句我马上处理。
```
