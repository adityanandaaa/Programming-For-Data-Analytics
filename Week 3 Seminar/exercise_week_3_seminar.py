import json
from urllib.parse import urlencode
from urllib.request import urlopen


def main() -> None:
	# Define the search keyword
	query = "Data Science"
	base_url = "https://openlibrary.org/search.json"
	all_pages_data = []
	
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
		
		# Store page data with page number
		all_pages_data.append({"page": page, "docs": docs})

	# Exit early if no results were found at all
	if not all_pages_data:
		print(f"No results found for '{query}'.")
		return

	# Calculate total results
	total_results = sum(len(page_data["docs"]) for page_data in all_pages_data)

	# Prepare output lines for console and file
	output_lines = []
	output_lines.append(f"Found {total_results} results across pages 1-3 for '{query}':\n")
	
	# Global counter for numbering across all pages
	global_idx = 1
	
	# Iterate through each page and its books
	for page_data in all_pages_data:
		page_num = page_data["page"]
		docs = page_data["docs"]
		
		# Add page separator
		output_lines.append(f"{'=' * 80}")
		output_lines.append(f"PAGE {page_num} - {len(docs)} results")
		output_lines.append(f"{'=' * 80}")
		output_lines.append("")
		
		# Iterate through each book on this page
		for book in docs:
			title = book.get("title", "Unknown title")
			authors = book.get("author_name", [])
			# Join multiple authors with commas or use "Unknown author" if none found
			author_text = ", ".join(authors) if authors else "Unknown author"
			
			# Format output lines for each book
			line1 = f"{global_idx}. Title: {title}"
			line2 = f"   Author(s): {author_text}"
			output_lines.append(line1)
			output_lines.append(line2)
			output_lines.append("")
			global_idx += 1
	
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
