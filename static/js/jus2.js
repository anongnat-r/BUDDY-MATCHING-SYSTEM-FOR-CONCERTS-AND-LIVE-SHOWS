$(document).ready(function () {
  var data = $.get('/config', function (config) {
    // console.log(config);

    firebase.initializeApp(config);

    if (document.readyState == "interactive") {

      firebase.auth().onAuthStateChanged(function (user) {

        var user = firebase.auth().currentUser;

        if (user != null) {
          user.providerData.forEach(function (profile) {
            
            
            // $.ajax({
            //   type: "POST",
            //   cache: false,
            //   data: {
            //     keyword: search_word
            //   },
            //   url: qurl,
            //   success: function (data) {
            //     console.log(data);
            //   },
            //   error: function (jqXHR) {
            //     // alert("error: " + jqXHR.status);
            //     console.log(jqXHR);
            //   }
            // })
            

            

            

            console.log("  Name: " + profile.displayName);
            console.log("  Photo URL: " + profile.photoURL);
            document.getElementById("user_name").innerHTML = profile.displayName;
            document.getElementById('user_img').src = profile.photoURL;

          });
        }


        // The user's ID, unique to the Firebase project. Do NOT use
        // this value to authenticate with your backend server, if
        // you have one. Use User.getToken() instead.
      });

      var btnLogout = document.getElementById('signOut');
      btnLogout.addEventListener('click', e => {
        firebase.auth().signOut().then(function () {
          console.log("signout successful!")
        }, function (error) {
          console.log("!!!signout fail!!!")


        })
      });
    }
  });


});




// document.onreadystatechange = function () {
//     console.log(config)
// }