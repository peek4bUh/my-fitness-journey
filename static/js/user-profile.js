var userProfile = document.getElementById('user-profile');
var userProfileDialog = document.getElementById('user-profile-dialog');

userProfile.addEventListener('click', () => {
  userProfileDialog.classList.toggle('hidden');
});
