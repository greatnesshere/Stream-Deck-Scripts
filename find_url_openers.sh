#!/bin/bash

# Path to lsregister
LSREGISTER='/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister'

# Find all applications that can open .url files
find_apps_that_open_url() {
    # List all applications and their supported document types
    "$LSREGISTER" -dump | grep -B 10 'uti:public.url' | grep -E '^path:|uti:public.url'
}

# Run the function
find_apps_that_open_url
