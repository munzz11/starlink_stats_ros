function recursive_for_loop { 
    for f in * ;  do 
        if [ -d $f  -a ! -h $f ];  
        then  
            cd -- "$f";  
            if [[ "$f" != *"pycache"* ]]; then
     	        # If it doesn't contain "pycache", touch __init__ to initialize as part of the python module
  	        touch __init__.py
            	# use recursion to navigate the entire tree
            	recursive_for_loop;
	    fi;
            cd ..; 
        fi;  
    done;  
};
cd ../src/spacex/
recursive_for_loop
cd ..
cd ..
