mailAddress = "john@n.yu.edu"
print(mailAddress.split("@"))
name= mailAddress.split("@")[0]
serverAndDomain = mailAddress.split("@")[1]
print(name)
print(serverAndDomain)
length = len(serverAndDomain.split("."))
server =serverAndDomain.split(".")[0:(length)-1]
domain=serverAndDomain.split(".")[length-1]
print(str(server))
print(domain)
