/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: SimonsArray
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "SimonsArray.hpp"

using namespace gen::arrays;

QDBusArgument &gen::arrays::operator<<(QDBusArgument &argument, const SimonsArray &object) {
    argument.beginStructure();
    argument << object.numbers;
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::arrays::operator>>(const QDBusArgument &argument, SimonsArray &object) {
    argument.beginStructure();
    argument >> object.numbers;
    argument.endStructure();
    return argument;
}

bool gen::arrays::operator!=(const SimonsArray &lhs, const SimonsArray &rhs) {
    return (false
        || lhs.numbers != rhs.numbers
    );
}

bool gen::arrays::operator!=(const QList<SimonsArray> &lhs, const QList<SimonsArray> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=0; i<lhs.size(); ++i) {
        if (lhs[i] != rhs[i]) {
            return true;
        }
    }
    return false;
}

SimonsArray SimonsArrayFactory::create (
    QList<StructArray> numbers
) const {
    return SimonsArray {
        .numbers = numbers,
    };
}

SimonsArray SimonsArrayFactory::create (
    QVariant numbers
) const {
    QList<StructArray> member_0;
    for (auto& item_0 : numbers.value<QVariantList>()) {
        StructArray o_0;
        o_0 = item_0.value<StructArray>();

        member_0.push_back(o_0);
    }

    return SimonsArray {
        .numbers = member_0,
    };
}

void SimonsArray::registerMetaTypes() {
    qRegisterMetaType<SimonsArray>("SimonsArray");
    qDBusRegisterMetaType<SimonsArray>();
    qDBusRegisterMetaType<QList<SimonsArray>>();
}