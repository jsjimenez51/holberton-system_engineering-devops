# Fix to a Wordpress settings file for the proper extension

exec { 'wp setting config':
  command  => 'sed -i \'s/phpp/php/\' /var/www/html/wp-settings.php',
  provider => 'shell'
}
