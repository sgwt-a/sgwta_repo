#ifndef SAMPLE_H
#define SAMPLE_H

// define sample class
class Sample{
    public:
        void set_private_num(int num);
        int get_private_num();
        int add_private_public();
        int add_private_public_external(int external_num);
        int public_num = -100;
    private:
        int private_num;
};

#endif // SAMPLE_H
