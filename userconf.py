import os

# User dir
def userDir(name):
    path = os.mkdir(f"{name}")
    return path


# Generate user config file
def writeUserConfig(fileConf, key, id: int) -> None:
    fileConf.write("[Interface]\n")
    fileConf.write("PrivateKey = {}\n".format(key))
    fileConf.write("Address = 10.0.0.{}/32\n".format(id))
    fileConf.write("DNS=8.8.8.8\n")

    fileConf.write("\n[Peer]\n")
    fileConf.write("PublicKey = vMNqR62ERN5XJNaKAnLssulQbDBStjiKXW8cesH9uWs=\n")
    fileConf.write("Endpoint = 3.64.163.246:55555\n")
    fileConf.write("AllowedIPs = 0.0.0.0/0\n")
    fileConf.write("PersistenKeepalive = 20\n")

# get userFile
def createFile(name,  id: int):
    UserPrivatekey = open(f"/etc/wireguard/{name}_privatekey", "r")
    wgConf = open(f"{userDir(name)/name}_wg.conf", "w")
    writeUserConfig(wgConf, UserPrivatekey, id)
    wgConf.close()

# Create qr code    
def createQR(fileConf, name):
    os.system(f"qrencode -t ansiutf8 < {fileConf} > {name}.png")



