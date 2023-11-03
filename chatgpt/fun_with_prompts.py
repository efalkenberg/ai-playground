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

def prompt_translate_hackernews(hackernews_html=""):

	# For consistent testing, the html will be passed in, in all other cases
	# we'll need to download it here. In production code you'd want to
	# cache the response here.
	if not hackernews_html:
		HACKERNEWS_URL = 'https://news.ycombinator.com/'
		hackernews_html = requests.get(HACKERNEWS_URL).text
		if len(hackernews_html) < 1:
			print_error(f"""Error downloading hackernews html code. 
			   Response was: {hackernews_html}
			   """)
			return

		## uncomment to update the static file that is being used for unit tests		
		# with open("tests/hackernews_html_test.txt", "w") as text_file:
		# 	text_file.write(hackernews_html)
		
		print_good("Downloaded hackernews html")

	# we could extract the links with a prompt like this but it turns out to be semi-reliable
	# prompt = f"""
	# Extract the links and the coresponding title from inside the <titleline> tags in ```{hackernews_data}```.
	# Translate the titles to German and renders as a list of links in markdown.
	# """
	#
	# Instead we'll do some pre-processing of the data before passing it into the model.
	# The risk is that if anything in the html changes, we are doomed. 
	# Not to myself: this is a very interesting trade-off
	#
	# the links are in the form of 
	# <span class="titleline"><a href="{url}" rel="noreferrer">{title}</a>
	# pattern = '<span class="titleline"><a href="(.*?)" rel="noreferrer">(.*?)</a>'
	link_pattern = re.compile(r'<span class="titleline"><a href="(.*?)">(.*?)</a>', re.I)

    # Find all matches in the HTML content
	matches = link_pattern.findall(hackernews_html)

    # Iterate through the matches and extract URL and title
	results = []
	for match in matches:
		results.append({
			# 'url' : match[0],
			'title' : match[1]
		})

	prompt = f""" Given the input json ```{results}```, extract all the title values.
	 Translate each of the titles to Spanish and German.
	 Render the result as a html table with the titles in all three languages.
	"""

	response = get_completion(prompt)
	display(HTML(response)) # in Jupyter this actually renders
	print(response)
	return response


def is_api_token_valid():
	api_key = os.getenv(API_KEY_NAME)
	if not api_key:
		print_error(f"No OpenAI API key found. Set as environment variable like `{API_KEY_NAME}=sk-.....`")
		return False
		
	print_good(f"OpenAI key found as environment variable under `{API_KEY_NAME}`")
	openai.api_key = api_key
	return True

def print_error(msg):
	print(f"💩 {msg}")

def print_good(msg):
	print(f"✅ {msg}")

def print_info(msg):
	print(f"⚠️ {msg}")

def main():
	if is_api_token_valid():
		prompt_translate_hackernews()

if __name__ == "__main__":
    main()