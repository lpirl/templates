``simple-pdf.rst`` features custom styles which enable highlighting text
with colors.

These colors can be used as an "internal markup" while authoring documents.
You can highlight words you want to replace, sentences that could be removed,
facts you want to double-check, etc.

To enable this "internal markup" compile with::

  rst2pdf --stylesheets=default.style,work-additions.style my-document.rst

To disable the "internal markup", compile with::

  rst2pdf --stylesheets=default.style my-document.rst
