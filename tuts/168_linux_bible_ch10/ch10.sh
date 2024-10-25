

# search for packages in Ubuntu repository (e.g. "python" package)
# apt = Advanced Packaging Tool  

apt search python

# By default, apt search command looks for the searched term in both the name of the package and its description.
# You may narrow down the search by instructing the apt command to search for package names only.

apt search --names-only python

# search for a command that is contained within some package on APT 
# "apt search <COMMAND>" 

# apt show = detailed information on a package
:'
You get:

    Version information
    Repository information
    Origin and maintainer of the package information
    Where to file a bug
    Download and installation size
    Dependencies
    Detailed description of the package
    And a lot more
' 
apt show python
apt info python	  # "info" = alias for show. (undocumented - for people who are used to "info" from red hat)

sudo apt install python


######  download packages without installing them. 
#  This is often used in cases where internet access on another computer is not available, and one needs to be able to sideload the packages onto the machine.

# Method 1: 
apt download PACKAGE_NAME

# Method 2: 
:'
STEP 1: Remove any packages currently saved in the cache by running sudo apt clean.
STEP 2: Include --download-only in the command, e.g: sudo apt install --download-only <PACKAGE_NAME>. This also works for multiple packages, e.g: sudo apt install --download-only <package1> <package2> <package3>
STEP 3: All packages downloaded via this method will be saved in the /var/cache/apt/archives directory. Youll be able to copy them to your desired location or leave them there for future sudo apt install operations.
'

# Uninstall a package: 
sudo apt remove package_name

