const { auth } = require('@utils');

exports.run = async (message, args) => {
   
    if (auth.isMod(message.member)) {
       
        // If user is a moderator, do something
       
    } else {
       message.reply('You must be a moderator or higher in order to run this command.');
    }
     
 };