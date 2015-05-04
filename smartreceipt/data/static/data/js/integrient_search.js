/* MiRo SmartReceipt 2015 */
function createReceiptDOM(receipt) {
	var articleteaser_single = document.createElement("div");  
	articleteaser_single.className = "articleteaser_single";
	
	// image
	var articleteaser_single_link = document.createElement('a');
	articleteaser_single_link.href = receipt.receipt_url;
	
	var articleteaser_single_image_div = document.createElement("div"); 
	articleteaser_single_image_div.className = "image"; 
	
	var articleteaser_single_image_div_image = document.createElement("img"); 
	articleteaser_single_image_div_image.src = receipt.receipt_image_url;
	articleteaser_single_image_div_image.name = "slide";
	articleteaser_single_image_div_image.id = "recipePreviewImage";
	articleteaser_single_image_div.appendChild(articleteaser_single_image_div_image);
	
	articleteaser_single_link.appendChild(articleteaser_single_image_div);
	
	articleteaser_single.appendChild(articleteaser_single_link);
	// image
	
	// headline
	var articleteaser_single_spitzmarke_div = document.createElement("div");
	articleteaser_single_spitzmarke_div.className = "spitzmarke";
	articleteaser_single.appendChild(articleteaser_single_spitzmarke_div);

	var articleteaser_single_headline_div = document.createElement("div");
	articleteaser_single_headline_div.className = "headline";

	var articleteaser_single_headline_link = document.createElement('a');
	articleteaser_single_headline_link.href = receipt.receipt_url;
	articleteaser_single_headline_link.appendChild(document.createTextNode(receipt.receipt_name));
	articleteaser_single_headline_div.appendChild(articleteaser_single_headline_link);

	articleteaser_single.appendChild(articleteaser_single_headline_div);
	// headline
	
	// teasertext
	var articleteaser_single_teasertext_div = document.createElement("div");
	articleteaser_single_teasertext_div.className = "teasertext";
	articleteaser_single_teasertext_div.appendChild(document.createTextNode(receipt.receipt_teaser));
	articleteaser_single.appendChild(articleteaser_single_teasertext_div);
	
	var articleteaser_single_teasertext_br = document.createElement("br");
	articleteaser_single.appendChild(articleteaser_single_teasertext_br);
	// teasertext
	
	// desc
	var articleteaser_single_receipt_link = document.createElement('a');
	articleteaser_single_receipt_link.href = receipt.receipt_url;
	articleteaser_single_receipt_link.appendChild(document.createTextNode("zum Rezept"));
	articleteaser_single.appendChild(articleteaser_single_receipt_link);
	
	var articleteaser_single_clear_both_div = document.createElement("div");
	articleteaser_single_clear_both_div.className = "clear_both";
	articleteaser_single.appendChild(articleteaser_single_clear_both_div);
	
	var articleteaser_single_line_div = document.createElement("div");
	articleteaser_single_line_div.className = "line";
	articleteaser_single.appendChild(articleteaser_single_line_div);
	// desc	
	
	return articleteaser_single;
}