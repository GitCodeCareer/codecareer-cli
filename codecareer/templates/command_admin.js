const { auth } = require('@utils');

exports.run = async (message, args) => {
   
    if (auth.isAdmin(message.member)) {
       
        // If user is an admin, do something
       
    } else {
       message.reply('You must be an admin in order to run this command.');
    }
     
 };