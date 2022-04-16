import os

# generate key users 
def genKey (name: str) -> None:
    os.system("wg genkey | tee {}_privatekey | wg pubkey | tee {}_publickey".format(name, name))


# simple generate code on config
def writeServerConfig(fileConf, key, id: int) -> None:
    fileConf.write("\n[Peer]\nPublicKey = {}AllowedIPs = 10.0.0.{}/32\n".format(key, id))


# add users on config file
def configFile(name, id: int):
    genKey(name)
    
    Userpublickey = open(f"{name}_publickey", "r")
    Userpublickey = Userpublickey.readline()
    
    config = open("new.conf", "a")
    writeServerConfig(config, Userpublickey, id)
    config.close()





