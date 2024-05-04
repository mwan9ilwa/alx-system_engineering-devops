# install_flask.pp

package { 'Flask':
  ensure   => '2.1.0',      # Ensure Flask version 2.1.0 is installed
  provider => 'pip3',       # Use pip3 as the package provider
  require  => Package['python3-pip'],  # Ensure python3-pip is installed first
}
