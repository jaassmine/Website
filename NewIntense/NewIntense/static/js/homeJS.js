$(document).ready(function(){
    function alignModal(){
        var modalDialog = $(this).find(".bg-modal");
        
        // Applying the top margin on modal dialog to align it vertically center
        modalDialog.css("margin-top", Math.max(0, ($(window).height() - modalDialog.height()) / 2));
        // modalDialog.css("margin-left", Math.max(0, ($(window).width() - modalDialog.width()) / 4));
    }
    // Align modal when it is displayed
    $(".bg-modal").on("shown.bs.modal", alignModal);
    
    // Align modal when user resize the window
    $(window).on("resize", function(){
        $(".modal:visible").each(alignModal);
    });   
});


document.getElementById('login_Button').addEventListener('click', function(){
    document.querySelector('.modal').style.display = 'flex';
});

document.querySelector('.close').addEventListener('click' , function(){
    document.querySelector('.modal').style.display = 'none';
});


const inputs = document.querySelectorAll(".input");

function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

function submitForm() {
    // Get the first form with the name
    // Usually the form name is not repeated
    // but duplicate names are possible in HTML
    // Therefore to work around the issue, enforce the correct index
    var frm = document.getElementsByid(findForm)[0];
    frm.submit(); // Submit the form
    frm.reset();  // Reset all form data
    return false; // Prevent page refresh
 }
