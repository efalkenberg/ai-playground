# ------------------------------------------------------------------
# A shortened version of https://docs.anthropic.com/en/docs/welcome
# as my personal cheat sheet
# ------------------------------------------------------------------
#
# Create a virtualenv, activate it and pip install `anthropic`
# python -m venv claude-env
# source claude-env/bin/activate
# pip install anthropic 
#
# To make this sample work, set your API key as env variable:
# export ANTHROPIC_API_KEY="<YOUR_API_KEY_HERE>"
# get your key here: https://console.anthropic.com/settings/keys
#
# run the curl below to verify everything is fine
# curl https://api.anthropic.com/v1/messages \
#         --header "x-api-key: $ANTHROPIC_API_KEY" \
#         --header "anthropic-version: 2023-06-01" \
#         --header "content-type: application/json" \
#         --data \
#     '{
#         "model": "claude-3-5-sonnet-20241022",
#         "max_tokens": 1024,
#         "messages": [
#             {"role": "user", "content": "Hello, world"}
#         ]
#     }'

import anthropic
from pprint import pprint

client = anthropic.Anthropic()

print("""
@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#########*******************************#####
@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%########**********************************###
@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######***************************************
@@@@@%%%%%%@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%######*****************************************
@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####**+++++++************************************
@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=::::.:........::-=+++****************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##+-:::................:::::-=+*************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+-::........::.:.......::::::::::=***********************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-::.:::::::::::::::::::::::::::----:=+********************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-::::--------==--:--:-:::::-:--------:---+******************
%%%########%%%%%%%%%%%%%%%%%%%%%%%%%#+:.:::------=*####**+=-:::::-----:-------:::--=****************
###############%%%%%%%%%%%%%%%%%%%#+=-:...::----=**+*##+*=-::::------=----::::::-----=**************
##################%%%%%%%%%%%%%%##+---:..:::::-=+++*****=:..::-::----:::::....:::-----=*************
################################+=-----:::::::::-----=-:..::::::::::.......:::::::::---=+***********
##############################+======++-::::::.::::.....::::::::::::..:::::::::----------+**********
*********###################*=======+++-:::::::..::.:::::::::::::::.::::::::::::::-:------++++++++++
*****************#######***===--====+===-::::::::::::::::::::::::::::::::::::::::-----:::--+++++++++
************************+=--==--=-===----::::::::::::::::--:::::::::::::--::----------:::--=++++++++
**********************=--==-----===------:..::::::::::::::::::::::::::::::--::::---==--::---=+++++++
******************++=-=+*+==--------:::-:::::.::::::::::::::::::::-----:--------======------=+++++++
***********++++++=---=*+==--------------:::::::::-::-:::----:----::::::-------=-=======--==-=+++++++
******++++++++=------=--------=====---=------------------------:-------------==++++++===--====++++++
****++++++++--:-:-==--------------==++++*+*===--------------------------:---=======++++====-==++++++
***+++++=-----:---------==++******########*-------====---==--=----------============+++++===-=++++++
***+++=::-:------=++*####**+++====--==+**+--------=-======+==========-===-======++*++++=+======+++++
****+-::-:--=+**#*+=-::::------===+**++=+=-=======+++**+++++******+=====++=========+++++++=====+++++
****=::-=+#####*************###*##****#####**********************+====-----=====++++++++===--==+++++
****=-+***#####**########******************+*********************+=+++==----++*+=++++++==++--=-++***
******************************************************++********+=----=========+++++**+==++====+****
****************************************************+++*********+-==--==+==++=--++**++++=+++===+****
***************************************************************+=---==--=+++++====+**+++=+++==+*****
***************************************************************+----:-=-===+=+*++++*++*+=++===+*####
*******+++++++*************************************************+-----::----=++=+++++==+++=+++++*####
**+++++++++++++++++++++++++++**********************************=-:---:::----===-=***+=+++=+++++*####
++++++++++++++++++++++++++++***************######**######******-------:-------===+***+=++=+++=++####
+++++++++++++++++++++++++**************#####################**+-:-:------====-=++++++++=+==++==+###%
++++++++++++************************#########################*+---:-=---=-===-=+**+=-=-+++=+===+###%
*********************************############################*+==------=+==++==+*+=------==++==+###%
******************************###############################*+--=-=---====++++*=-:--=-----=+++=*##%
***************************##################################*=:-:---:----+*+=++-.:===---===++==*###
*************#####*****######################################*=::-------==+++++=:--:-=-:-==+++==*###
#############################################################+------=-==+***+--:---:::----=++=-=*###
############################################################*-:-:::==++***++=:-==--:::-:-==++===+###
#############################################%%%############=-::---+++++++=--=+===-::-::-=++==+=+###
###########################%%%%%%#########%%%%%%%##########*--:::-=++=+=+=:-===:-:----:-=+++=+==*###
########################%%%%%%%%%%%######%%%%%%%%%%%######*--:::--=+=====--===-::-==---======+==**##
##################%%%%%%%%%%%%%%%%%#####%%%%%%%%%%########+:--:::==--==-::--::.::==-:===+=+=++++**##
###################%#%%%%%%%%%###########%%%%%############+--::::-:-=-::-=::::::--=-=-=+++=++==+**##
#########################################################*-::::::--=-----::::.::-====-===+++==+***##
#########################################################*=:::::-------:::-=:.::-==-:-==++++==+**###   
""")
question = input("Ask me anything!:")

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    temperature=1,
    system="""You are a silly goose, so your answers are annoyingly silly.
    Because you are a goose, your answers include various loud honks, barks, 
    and cackles. Also some hisses.
    """,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{question}?"
                }
            ]
        }
    ]
)
print(message.content[0].text)