IFS=
RELEASE_FILE='ReleaseNotes.md'

fetchCommitByType() {
	# write subheading for the release note
	writeSubheadersToFile $1

	# iterate each line of logs that are filtered by types
	local IFS=$'\n'
	for line in $(git log --grep=$1 --pretty=format:"%s" | sed '/^\s*$/d'); do
		# local IFS=:
		# read -r -a sections <<< "$line"
		# write commit messages to the release note
		writeSectionsToFile $line
	done
}

writeSectionsToFile() {
	# scope=$(echo ${sections[0]} | sed 's/.*(\(.*\))/\1/')
	# subject=${sections[1]}
	# comment=${sections[2]}
	feature_scope=$(cut -d ':' -f 1 <<< $1)
	scope=$(echo $feature_scope | sed 's/.*(\(.*\))/\1/')
	subject=$(cut -d ':' -f 2 <<< $1)		
	echo "* **$scope**:$subject" >> $RELEASE_FILE
}

writeSubheadersToFile() {
	case $1 in
		feat)
			echo "#### New Features" >> $RELEASE_FILE
			;;
		fix)
			echo "#### Bug Fixes" >> $RELEASE_FILE
			;;
		test)
			echo "#### Tests" >> $RELEASE_FILE
			;;
	esac
}

> $RELEASE_FILE
echo "## RELEASE NOTES" >> $RELEASE_FILE
echo '' >> $RELEASE_FILE
fetchCommitByType 'feat'
echo '' >> $RELEASE_FILE
fetchCommitByType 'fix'
echo '' >> $RELEASE_FILE
fetchCommitByType 'test'
