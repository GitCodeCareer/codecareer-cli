const { auth } = require('@utils');

exports.run = async (message, args) => {
   
    if (auth.isOwner(message.member)) {
       
        // If user is the guild owner, do something
       
    } else {
       message.reply('You must be the guild owner in order to run this command.');
    }
     
 };