#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import openai


def main(apikey):
    openai.api_key = apikey
    inputSTR = ""
    loop = True
    while loop:
        if inputSTR == "\quit":
            loop = False
        else:
            if inputSTR == "":
                inputSTR = input("ChatGPT>>> Hello, I am your AI grammar teacher today.\nHuman:")
                result = ""
            else:
                if result == "":
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are an English teacher."},
                              {"role": "assistant", "content": "Correct my grammatical error if possible."},
                              {"role": "assistant", "content": "If there is no grammatical error, chat with me."},
                              {"role": "user", "content": "{}".format(inputSTR)},
                              ],
                    )
                    for choice in response.choices:
                        result += choice.message.content
                    inputSTR = input("\n\nChatGPT>>>{}\nHuman:".format(result))
                    result = ""
                else:
                    pass

    return None


if __name__ == "__main__":
    try:
        with open("account.info") as f:
            accountDICT = json.load(f)
        if accountDICT["openai_api_key"] == "":
            print("account.info 檔內沒有填入有效的 Openai apikey!")
        else:
            pass
    except:
        print("沒有 account.info 檔，或是沒有填入有效的 Openai apikey!")

    main(accountDICT["openai_api_key"])