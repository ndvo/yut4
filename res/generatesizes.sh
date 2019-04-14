original='drawable-xxxhdpi';
if [ -d $original ];
	then
		tresquartos='drawable-xxhdpi';
		metade='drawable-xhdpi';
		umquarto='drawable-hdpi';
		smallest='drawable';
		if ! [ -d $tresquartos ];
			then
				mkdir $tresquartos;
				mkdir $metade;
				mkdir $umquarto;
				mkdir $smallest;
			else
				echo "As pastas já estão criadas";
			fi;
		for i in $original/*.{png,jpg,gif,jpeg}; 
			do if [ -s "$i" ]
				then
					echo Tratando $i;
					imagem=`echo "$i"|sed -e "s/$original\///"`;
					convert "$i" -resize 75% $tresquartos/"$imagem";
					convert "$i" -resize 50% $metade/"$imagem";
					convert "$i" -resize 37.5% $umquarto/"$imagem";
					convert "$i" -resize 25% $smallest/"$imagem";

			fi;
			done;
	else
		echo "Não há um diretório $original nesta pasta";
fi;
