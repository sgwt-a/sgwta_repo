#ifndef RAT_H
#define RAT_H

class Rat {
    public:
        Rat();
        ~Rat();
        static void showNum();
        void squeak();
        static int countPublic_;
    private:
        int id_;
        static int count_;
};


#endif // RAT_H
