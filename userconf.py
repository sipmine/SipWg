import os
from safe import SERVER_PUBLIC_KEY, SERVER_IP
# User dir
def userDir(name):
    path = os.mkdir(f"{name}")
    return path


# Generate user config file
def writeUserConfig(fileConf, key, id: int) -> None:

    fileConf.write(f'''[Interface] \n PrivateKey = {key} \n Address = 10.0.0.{id}/32 \n DNS=8.8.8.8 \n [Peer] \n PublicKey = {SERVER_PUBLIC_KEY} \n Endpoint = {SERVER_IP} \n AllowedIPs = 0.0.0.0/0 \n PersistenKeepalive = 20''')
# key, id, server ip
# get userFile
def createFile(name, id: int):
    UserPrivatekey = open(f"{name}_privatekey", "r")
    UserPrivatekey = UserPrivatekey.readline()
    wgConf = open(f"{name}_wg.conf", "w")
    writeUserConfig(wgConf, UserPrivatekey, id)
    wgConf.close()

# Create qr code    
def createQR(fileConf, name):
    os.system(f"qrencode -t ansiutf8 < {fileConf} > {name}.png")



