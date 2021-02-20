def convert(dic):
	full_html = ""

	for i in range(0, len(dic)):
		header = dic[i]["header"]
		detail = dic[i]["detail"]
		link = dic[i]["link"]
		header = "<a href=\"" + link + "\">" + header + "</a><br/>"
		html_str = header + detail + "<br/>"
		full_html = full_html + "<p>" + html_str + "<p/>"
	return full_html