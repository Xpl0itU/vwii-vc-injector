from genericpath import isfile
import shutil
import os
import hashlib
title_key = "Kirby Epic Yarn EUR TITLEKEY"
if hashlib.md5(title_key.encode()).hexdigest() != "65c8d67b533d8840f2727155fb21b0fa":
    print("Please edit this file and replace title_key with the Kirbys Epic Yarn EUR Titlekey")
    exit()
files = {
    "/code/deint.txt",
    "/code/font.bin",
    "/code/c2w.img",
    "/code/boot.bin",
    "/code/dmcu.d.hex",
    "/code/cos.xml",
    "/code/frisbiiU.rpx",
    "/code/fw.img",
    "/code/fw.tmd",
    "/code/htk.bin",
    "/code/nn_hai_user.rpl",
    "/content/assets/shaders/cafe/banner.gsh",
    "/content/assets/shaders/cafe/fade.gsh*",
    "/meta/bootMovie.h264",
    "/meta/bootLogoTex.tga",
    "/meta/bootSound.btsnd"
}


if(not(os.path.exists("bin/Kirby's Epic Yarn [VARP01]"))):
    for file in files:
        print(file)
        os.system("cd bin && java -jar JNUSTool.jar 00050000101b1800 "+ title_key + " -file " + file)

if(os.path.exists("bin/tickets")):
    shutil.rmtree("bin/tickets")

os.system("cd bin && ./wit extract game.wbfs --psel data --psel -update --files +tmd.bin --files +ticket.bin --dest tickets -vv1")
os.rename("bin/tickets/ticket.bin", "bin/tickets/rvlt.tik")
os.rename("bin/tickets/tmd.bin", "bin/tickets/rvlt.tmd")

os.system("cd bin && ./wit copy -I game.wbfs Kirby\\'s\ Epic\ Yarn\ [VARP01]//content//game.iso")
shutil.copyfile("bin/nfs2iso2nfs", r"bin/Kirby's Epic Yarn [VARP01]/content/nfs2iso2nfs")
shutil.copyfile("bin/wii_common_key.bin", r"bin/Kirby's Epic Yarn [VARP01]/content/wii_common_key.bin")
os.system("cd bin/Kirby\\'s\ Epic\ Yarn\ [VARP01]/content/ && chmod 777 nfs2iso2nfs && ./nfs2iso2nfs -iso game.iso")
os.remove(r"bin/Kirby's Epic Yarn [VARP01]/content/nfs2iso2nfs")
os.remove(r"bin/Kirby's Epic Yarn [VARP01]/content/wii_common_key.bin")
os.remove(r"bin/Kirby's Epic Yarn [VARP01]/content/game.iso")
# TODO: NUSpacker and stuff