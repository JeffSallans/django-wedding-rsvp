$(function () {

	alert(rsvpObject);

	function GetURLParameter(sParam)
	{
	    var sPageURL = window.location.search.substring(1);
	    var sURLVariables = sPageURL.split('&');
	    for (var i = 0; i < sURLVariables.length; i++) 
	    {
	        var sParameterName = sURLVariables[i].split('=');
	        if (sParameterName[0] == sParam) 
	        {
	            return sParameterName[1];
	        }
	    }
	}

	var rsvpBox = function() {
		var scope = this;


		//Form variables
		scope.nameOfParty = ko.observable("none");
		scope.isAttending = ko.observable(true);

		var numberOfPossibleAttendees = ko.observable(0);
		scope.possibleAttendeesOptions = ko.computed(function() {
			var resultArray = [];
			for (var i = 1; i <= numberOfPossibleAttendees(); i++) {
				resultArray.push(i);
			};
			return resultArray;
		})
		scope.numberAttending = ko.observable(undefined);

		scope.visibleSetting = function() {

			if (isAttending()) return "visible";
			return "hidden";
		};

		//Used to convert URL parameters into inital form values
		scope.parseUrlParam = function() {

			var queryString = GetURLParameter("q") || '';

			var nameAndNumber = $.parseParams( decodeURIComponent( window.atob(queryString)));

			scope.nameOfParty(nameAndNumber.name);

			numberOfPossibleAttendees(nameAndNumber.number);
		};

		scope.submit = function() {

			if (scope.isAttending() && !scope.numberAttending()) {

				alert("Please Select Number Attending.");
				return;
			}

			alert("ajax call");
		}

		return scope;
	}();

	ko.applyBindings(rsvpBox);

	rsvpBox.parseUrlParam();
});