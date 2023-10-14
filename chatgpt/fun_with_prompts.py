import openai
import os
import requests
import re
from IPython.display import display, HTML

API_KEY_NAME = 'OPEN_AI_KEY'

# sample wrapper from deeplearning.ai
def get_completion(prompt, model="gpt-3.5-turbo",temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def prompt_translate_hackernews():

	# we will read the data into a string first:
	HACKERNEWS_URL = 'https://news.ycombinator.com/'
	hackernews_data = requests.get(HACKERNEWS_URL).text

	# we could extract the links with a prompt like this but it turns out to be semi-reliable
	# prompt = f"""
	# Extract the links and the coresponding title from inside the <titleline> tags in ```{hackernews_data}```.
	# Translate the titles to German and renders as a list of links in markdown.
	# """

	# the links are in the form of 
	# <span class="titleline"><a href="{url}" rel="noreferrer">{title}</a>
	# pattern = '<span class="titleline"><a href="(.*?)" rel="noreferrer">(.*?)</a>'
	link_pattern = re.compile(r'<span class="titleline"><a href="(.*?)">(.*?)</a>', re.I)

    # Find all matches in the HTML content
	matches = link_pattern.findall(hackernews_data)

    # Iterate through the matches and extract URL and title
	results = []
	for match in matches:
		results.append({
			# 'url' : match[0],
			'title' : match[1]
		})

	prompt = f""" Given the input json ```{results}```, extract all the title values.
	 Translate each of the titles to spanish.
	 Render the result as a html table.
	"""

	response = get_completion(prompt)
	display(HTML(response)) # in Jupyter this actually renders
	print(response)


def is_api_token_valid():
	api_key = os.getenv(API_KEY_NAME)
	if not api_key:
		print(f"💩 No OpenAI API key found. Set as environment variable like `{API_KEY_NAME}=sk-.....`")
		return False
		
	print(f"✅ OpenAI key found as environment variable under `{API_KEY_NAME}`")
	openai.api_key = api_key
	return True

def main():
	if is_api_token_valid():
		prompt_translate_hackernews()

if __name__ == "__main__":
    main()