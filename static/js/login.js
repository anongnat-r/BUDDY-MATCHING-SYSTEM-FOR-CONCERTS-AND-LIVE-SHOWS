
$(document).ready(function(){
    var data = $.get('/config', function(config) {
      
      
      firebase.initializeApp(config);

      // document.onreadystatechange = function () {
      //   console.log('1')
        if (document.readyState == "interactive") {
            console.log("a")
          var uiConfig = {
            signInSuccessUrl: '/signin',
            signInOptions: [
              
              // Leave the lines as is for the providers you want to offer your users.
              
              firebase.auth.TwitterAuthProvider.PROVIDER_ID,
  
            ],
            // tosUrl and privacyPolicyUrl accept either url string or a callback
            // function.
            // Terms of service url/callback.
            tosUrl: '<your-tos-url>',
            // Privacy policy url/callback.
            privacyPolicyUrl: function () {
              window.location.assign('<your-privacy-policy-url>');
            }
          };
  
          // Initialize the FirebaseUI Widget using Firebase.
          var ui = new firebaseui.auth.AuthUI(firebase.auth());
          // The start method will wait until the DOM is loaded.
          
          
          ui.start('#firebaseui-auth-container', uiConfig);
        }
      // }  
    });
      
  });  
  