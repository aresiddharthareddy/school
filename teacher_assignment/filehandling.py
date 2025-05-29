filein = ("D:\python practice\\test_practice\sample.txt")
def filehandling(filein):

    f=open(filein,"w")
    f.write("This is a sample text.\nItcontains some sample text for testing.\nThis text is just for testing purposes")
    f.close()

    f=open(filein,"r")
    print(f.read())

    f=open(filein,"r+")
    content=f.read().replace("test","tezt")
    f.seek(0)
    f.write(content)
    f=open(filein,"r")
    return f.read()

files= filehandling(filein)
print(files)
