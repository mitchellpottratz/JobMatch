
const $skillSearchResultContainer = $('#skills-results-container')
const $skillSearchResults = $('#skill-search-results')

// listens for change in the find skills input text
$('#skill-search').keyup(function(e) {
	console.log(e.keycode)
	if ($(this).val().length <= 1 && e.keycode === 8 || e.keycode === 46) {
		console.log('results should hide')
		$skillSearchResultContainer.hide()
	} else {
		console.log('results should not hide')
		$skillSearchResultContainer.show()
	}

	// sends a request to search for skills based on the current 
	// value of the skill search input
	$.ajax({
        url: '/skills/search/',
        data: {
          'skill_string': $(this).val()  
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
	        	$skillSearchResultsContainer.hide()
	        }		        	
        }
	})	
})

// when the user leaves the skill search input
$('#skill-search').focusout(function() {
	// hide the search results
	$skillSearchResultContainer.hide()
}) 

// listens for a skill result to be clicked
$('#skill-search-results').on('click', function(e) {
	$('#skill-search').val($(e.target).text())
	$skillSearchResultContainer.hide()
})

// listens for the add skill button to be clicked
$('#add-skill-btn').on('click', (e) => {
	e.preventDefault()
	const skillText = $('#skill-search').val()
	$('#skill-search').val('')
	const $skill = $('<span class="badge badge-primary mr-1 p-2">' + skillText + '</span>')
	$('#added-skills-container').append($skill)

	const $selectedSkill = $('#skills-hidden-input option').filter(function(i, e) { 
		return $(e).text() === skillText
	})
	$selectedSkill.prop('selected', true)
})



