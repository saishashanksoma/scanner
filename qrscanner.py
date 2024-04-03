import qrcode
myqr = qrcode.make("https://drive.google.com/file/d/1MIdZm7njHQlWEZQ3F5bJgwJfn3IukglJ/view?usp=sharing")
myqr.save("myqr.png")