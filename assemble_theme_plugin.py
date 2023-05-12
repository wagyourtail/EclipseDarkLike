#
# Author: Wagyourtail
# Created: 5/12/2023
#
# The purpose of this script is to assemble an Intellij .icls theme file
# into a .jar plugin file that can be installed into Intellij.
#
#

import sys, os, shutil, re
from zipfile import ZipFile

def package(file, version, vendorInfo, changeFile, descFile):
    (vendor, email, url) = vendorInfo

    # remove file ext from file
    fname = file[:file.rfind(".")]
    fext = file[file.rfind(".")+1:]

    if fext != "icls":
        raise Exception("File must be an .icls file")

    # remove old build dir
    if os.path.exists("./build"):
        shutil.rmtree("./build")

    # create unpacked plugin directory
    os.mkdir("./build")
    os.mkdir(f"./build/{fname}")
    os.mkdir(f"./build/{fname}/META-INF")
    os.mkdir(f"./build/{fname}/colors")

    # read theme name from xml
    with open(file, "r") as f:
        # read first line
        line = f.readline()
        match = re.search(r"name=\"(.*?)\"", line)
        if match:
            theme_name = match.group(1)
        else:
            raise Exception("Theme name not found")

    # copy color to unpacked plugin directory
    shutil.copy(file, f"./build/{fname}/colors/{theme_name}.xml")

    # read desc and change
    with open(descFile, "r") as f:
        descr = f.read()
    with open(changeFile, "r") as f:
        change = f.read()

    # create plugin.xml
    with open(f"./build/{fname}/META-INF/plugin.xml", "w") as f:
        f.write(f"""
<idea-plugin>
    <id>color.scheme.{theme_name}</id>
    <name>{theme_name} Color Scheme</name>
    <version>{version}</version>
    <vendor email="{email}" url="{url}">{vendor}</vendor>
    
    <description><![CDATA[
{descr}
    ]]></description>
    
    <change-notes><![CDATA[
{change}
    ]]></change-notes>
    
    <idea-version since-build="142.0"/>
    
    <depends>com.intellij.modules.lang</depends>
    
    <extensions defaultExtensionNs="com.intellij">
      <bundledColorScheme path="/colors/{theme_name}" />
    </extensions>
</idea-plugin>
    """)

    with ZipFile(f"./build/{fname}.jar", "w") as zip:
        for root, dirs, files in os.walk(f"./build/{fname}"):
            for file in files:
                zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(f"./build/{fname}")))




if __name__ == "__main__":
    package("EclipseDarkLike.icls", sys.argv[1], ("Wagyourtail", "wagyourtail@wagyourtail.xyz", "https://github.com/wagyourtail/EclipseDarkLike"), "change.md", "desc.md")