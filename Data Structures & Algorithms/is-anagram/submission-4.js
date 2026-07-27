class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // if(s.length !== t.length){
        //     return false
        // }
        const sorted1 = [...s].sort().join('')
        const sorted2 = [...t].sort().join('')
        return sorted1 === sorted2
    }

}
