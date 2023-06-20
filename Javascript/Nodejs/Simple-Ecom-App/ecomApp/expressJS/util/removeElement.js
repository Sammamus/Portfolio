const removeElement = (arrayIndex, arraySubject) => {
    if (arrayIndex == 0) {
        return arraySubject.slice(arrayIndex+1);
    } else if (arrayIndex + 1 == arraySubject.length) {
        arraySubject.pop();
        return arraySubject;
    } else {
        let firstHalf = arraySubject.slice(0, arrayIndex);
        let secondHalf = arraySubject.slice(arrayIndex+1);

        return firstHalf.concat(secondHalf);
    }
}

module.exports = removeElement;