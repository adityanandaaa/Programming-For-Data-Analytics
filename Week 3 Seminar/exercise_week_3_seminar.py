import json
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_book_data(query: str) -> dict:
	# Define the Open Library API endpoint
	base_url = "https://openlibrary.org/search.json"
	
	# Set query parameters with specific fields to retrieve
	# Parameters:
	#   - q: Search query string (the book title or keyword to search for)
	#   - fields: Comma-separated list of fields to return (title, author_name, etc.)
	#   - limit: Maximum number of results to return per request (10 in this case)
	params = {
		"q": query,
		"fields": "title,author_name,first_publish_year,key",
		"limit": 10,
	}
	
	# Encode parameters into the URL
	url = f"{base_url}?{urlencode(params)}"

	# Make HTTP request to the API with a 15-second timeout
	with urlopen(url, timeout=15) as response:
		payload = response.read().decode("utf-8")

	# Parse the JSON response
	data = json.loads(payload)
	docs = data.get("docs", [])
	
	# Return empty result if no documents found
	if not docs:
		return {"query": query, "result": None}

	# Return the first document and its metadata
	return {"query": query, "result": docs[0]}


def main() -> None:
	# Define the search keyword
	query = "Data Science"
	base_url = "https://openlibrary.org/search.json"
	all_docs = []
	
	# Fetch results from pages 1 through 3
	for page in range(1, 4):
		# Build parameters for pagination using the page parameter
		# Parameters:
		#   - q: Search query (same keyword "Data Science")
		#   - fields: Specific fields to retrieve from each result
		#   - page: Page number for pagination (1, 2, or 3 in this loop)
		#     Note: page parameter starts at 1, not 0
		params = {
			"q": query,
			"fields": "title,author_name,first_publish_year,key",
			"page": page,
		}
		
		# Construct and encode the full URL
		url = f"{base_url}?{urlencode(params)}"

		# Request data from the API
		with urlopen(url, timeout=15) as response:
			payload = response.read().decode("utf-8")

		# Parse the JSON response
		data = json.loads(payload)
		docs = data.get("docs", [])
		
		# Break the loop if no results found on this page
		if not docs:
			print(f"No more results at page {page}.")
			break
		
		# Accumulate all documents from all pages
		all_docs.extend(docs)

	# Exit early if no results were found at all
	if not all_docs:
		print(f"No results found for '{query}'.")
		return

	# Prepare output lines for console and file
	output_lines = []
	output_lines.append(f"Found {len(all_docs)} results across pages 1-3 for '{query}':\n")
	
	# Iterate through each book and extract title and authors
	for idx, book in enumerate(all_docs, start=1):
		title = book.get("title", "Unknown title")
		authors = book.get("author_name", [])
		# Join multiple authors with commas or use "Unknown author" if none found
		author_text = ", ".join(authors) if authors else "Unknown author"
		
		# Format output lines for each book
		line1 = f"{idx}. Title: {title}"
		line2 = f"   Author(s): {author_text}"
		output_lines.append(line1)
		output_lines.append(line2)
		output_lines.append("")
	
	# Combine all output lines into a single string
	output_text = "\n".join(output_lines)
	
	# Display results to console
	print(output_text)
	
	# Write results to a text file in the current directory
	output_file = "data_science_results.txt"
	with open(output_file, "w", encoding="utf-8") as f:
		f.write(output_text)
	
	# Confirm file creation
	print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
	main()
