const { auth } = require('@utils');

exports.run = async (message, args) => {
   
    if (auth.isRole('role')) {
       
        // If user is of a specific role, do something
       
    } else {
       message.reply('You must be a <ROLE> in order to run this command.');
    }
     
 };