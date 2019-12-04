for i in *.xml; do
sed  -i '2i <?xml-stylesheet type="text/css" href="NetworkProfile_Stylesheet.css"?>' "$i"
done