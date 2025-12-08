let userProfile = document.getElementById('user-profile');
let userProfileDialog = document.getElementById('user-profile-dialog');

userProfile.addEventListener('click', () => {
  userProfileDialog.classList.toggle('hidden');
});
