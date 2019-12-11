
const $skillSearchResultContainer = $('#skills-results-container')
const $skillSearchResults = $('#skill-search-results')

// listens for change in the find skills input text
$('#skill-search').keyup(function(e) {

	// if there is nothing in the search input and the user hit the backpace
	// or delete keys, the search results box is hidden
	if ($(this).val().length < 1 && e.keyCode === 8 || e.keyCode === 46) {
		$skillSearchResultContainer.hide()

	// otherwise show the search results box
	} else {
		$skillSearchResultContainer.show()
	}

	// sends a request to search for skills based on the current 
	// value of the skill search input
	$.ajax({
        url: '/skills/search/',
        data: {
          'skill_string': $(this).val(),

          // if a company user is searching then this is a 
          // job post id, otherwise its empty
          'data_id': $(this).attr('dataId')   
        },
        dataType: 'json',
        success: function (data) {
    		// emptys search results div
        	$skillSearchResults.empty()

        	// if there are search results
        	if (data.results.length > 0) {
	        	// iterate through all of the results
	        	data.results.forEach((result) => {
		        	const $skill = $('<div class="skill-result"></div>')
		        	const $skillText = $('<p>' + result + '</p>')
		        	$skillText.text(result)
		        	$skill.append($skillText)
		        	$skillSearchResults.append($skill)
	        	})

	        // if there are no results
	        } else {
	        	// hides the results container
	        	$skillSearchResultContainer.hide()
	        }		        	
        }
	})	
})

// listens for a skill result to be clicked
$('#skill-search-results').on('click', function(e) {
    $skillSearchResultContainer.hide()
})

// listens for a skill result to be clicked
$('#skill-search-results').on('click', function(e) {
	$('#skill-search').val($(e.target).text())
	$skillSearchResultContainer.hide()
})

// holds the text of the skill being hovered over
let skillText

// holds the width of the badge that is being hovered
let skillBadgeWidth

// listens for the mouse to enter or leave a skill badge
$('.skill-badge').hover(

    // function excecutes when the mouse enters
    function() {
        skillText = $(this).text().trim()
        skillBadgeWidth = $(this).css('width')
        $(this).addClass('skill-badge-hover')
        $(this).css('width', skillBadgeWidth)
        $(this).html('<i class="fas fa-trash-alt"></i>')

    // function executes when the mouse leaves
    }, function() {
        $(this).removeClass('skill-badge-hover')
        $(this).text(skillText)
    })

// listens for a skill badge to be clicked    
$('.skill-badge').on('click', function() {
    const $skillBadge = $(this)
    // make ajax call to delete the skill
    $.ajax({
        url: '/skills/delete/' + skillText + '/',
        method: 'POST',
        data: {
          'data_id': $(this).attr('dataId'),
          'csrfmiddlewaretoken': $skillBadge.attr('csrfToken')
        },
        dataType: 'json',
        success:function(data) {
            // removes the skill from the DOM
            $skillBadge.remove()

            // removes the skills parent element from the DOM
            $skillBadge.parent().remove()

            // shows a notification
            showNotification(data.message, '#skillNotification')
        }
    })
})

// shows a notification
showNotification = (text, id) => {
    $(id).text(text)
    $(id).fadeIn(500)

    // hides the notification after 2 seconds
    setTimeout(function(){
        $('.notification').fadeOut(500)
    }, 2000)
}
















