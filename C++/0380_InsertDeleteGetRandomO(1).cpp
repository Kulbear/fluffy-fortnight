class RandomizedSet
{
  private:
    vector<int> arr;
    unordered_map<int, int> m_;

  public:
    /** Initialize your data structure here. */
    RandomizedSet() {}

    /** Inserts a value to the set. Returns true if the set did not already
   * contain the specified element. */
    bool insert(int val)
    {
        if (m_.count(val))
            return false;
        m_[val] = arr.size();
        arr.push_back(val);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the
   * specified element. */
    bool remove(int val)
    {
        if (!m_.count(val))
            return false;
        int idx = m_[val];
        m_[arr.back()] = idx;
        m_.erase(val);
        std::swap(arr[idx], arr.back());
        arr.pop_back();
        return true;
    }

    /** Get a random element from the set. */
    int getRandom() { return arr[rand() % arr.size()]; }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
