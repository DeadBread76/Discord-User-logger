import discord
import asyncio

token = 'Token Here'
client = discord.Client()

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

@client.event
async def on_ready():
    print ("-----------------")
    print ("Logged in.")
    print ("-----------------")
    await main()
async def main():
    SERVER = input ("Server ID: ")
    print ("-----------------")
    server = client.get_server(SERVER)
    with open (server.name + " users.txt","w+") as handle:
        handle.write ("-----------------\n")
        handle.write (strip_non_ascii(server.name)+"\n")
    for member in server.members:
        print (member)
        with open (server.name + " users.txt","a+") as handle:
            handle.write ("-----------------\n")
            try:
                handle.write ("User: " + strip_non_ascii(str(member))+'\n')
            except Exception as u:
                print (u)
            handle.write ("User ID: " + str(member.id)+'\n')
            
    end = input('Press enter to do another, or type "quit" to quit.')
    if end.lower() == 'quit':
        await client.logout()
    else:
        await main()
        
client.run(token, bot=False)
