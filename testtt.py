write_config = configparser.ConfigParser()

write_config.add_section("Section1")
write_config.set("Section1","name","Jane")

cfgfile = open("sample.ini",'w')
write_config.write(cfgfile)
cfgfile.close()

SAMPLE.INI
[Section1]
name = Jane

read_config = configparser.ConfigParser()
read_config.read("sample.ini")

name = read_config.get("Section1", "name") #config check study
print(name)
