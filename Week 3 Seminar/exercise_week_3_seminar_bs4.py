import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main() -> None:
	# Define the search keyword and base URL
	query = "data science"
	base_url = "https://openlibrary.org/search"
	all_pages_data = []
	
	# Fetch results from pages 1 through 3
	# Parameters:
	#   - q: Search query keyword
	#   - mode: Search mode (everything searches across all fields)
	#   - page: Page number for pagination (1, 2, or 3 in this loop)
	for page in range(1, 4):
		# Construct the URL with query parameters
		url = f"{base_url}?q={query.replace(' ', '+')}&mode=everything&page={page}"
		
		# Make HTTP request and fetch the HTML content
		with urlopen(url, timeout=15) as response:
			html_content = response.read().decode("utf-8")
		
		# Parse the HTML with BeautifulSoup
		soup = BeautifulSoup(html_content, "html.parser")
		
		# Find all book result containers
		# Books are contained in elements with class "searchResultItem"
		result_items = soup.find_all("li", class_="searchResultItem")
		
		# Break if no results found on this page
		if not result_items:
			print(f"No more results at page {page}.")
			break
		
		# Extract title and author from each result
		page_books = []
		for item in result_items:
			# Find the book title within the resultTitle div
			title_div = item.find("div", class_="resultTitle")
			if title_div:
				title_link = title_div.find("a", class_="results")
				title = title_link.get_text(strip=True) if title_link else "Unknown title"
			else:
				title = "Unknown title"
			
			# Find the author information within the bookauthor span
			author_span = item.find("span", class_="bookauthor")
			if author_span:
				# Extract all author names from anchor tags within the span
				author_links = author_span.find_all("a")
				authors = [link.get_text(strip=True) for link in author_links]
				author_text = ", ".join(authors) if authors else "Unknown author"
			else:
				author_text = "Unknown author"
			
			# Store the book information
			page_books.append({"title": title, "authors": author_text})
		
		# Store page data with page number
		all_pages_data.append({"page": page, "books": page_books})
	
	# Exit early if no results were found at all
	if not all_pages_data:
		print(f"No results found for '{query}'.")
		return
	
	# Calculate total results
	total_results = sum(len(page_data["books"]) for page_data in all_pages_data)
	
	# Prepare output lines for console and file
	output_lines = []
	output_lines.append(f"Found {total_results} results across pages 1-3 for '{query}':\n")
	
	# Global counter for numbering across all pages
	global_idx = 1
	
	# Iterate through each page and its books
	for page_data in all_pages_data:
		page_num = page_data["page"]
		books = page_data["books"]
		
		# Add page separator
		output_lines.append(f"{'=' * 80}")
		output_lines.append(f"PAGE {page_num} - {len(books)} results")
		output_lines.append(f"{'=' * 80}")
		output_lines.append("")
		
		# Format each book entry
		for book in books:
			line1 = f"{global_idx}. Title: {book['title']}"
			line2 = f"   Author(s): {book['authors']}"
			output_lines.append(line1)
			output_lines.append(line2)
			output_lines.append("")
			global_idx += 1
	
	# Combine all output lines into a single string
	output_text = "\n".join(output_lines)
	
	# Display results to console
	print(output_text)
	
	# Write results to a text file in the current directory
	output_file = "data_science_results_bs4.txt"
	with open(output_file, "w", encoding="utf-8") as f:
		f.write(output_text)
	
	# Confirm file creation
	print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
	main()
