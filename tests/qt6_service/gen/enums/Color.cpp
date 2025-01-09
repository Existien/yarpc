/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Color
 *   Template: qt6/enum_source.j2
 */
#include "Color.hpp"

using namespace gen::enums;

QDBusArgument &gen::enums::operator<<(QDBusArgument &argument, const Color::Type &object) {
    argument << static_cast<int>(object);
    return argument;
}

const QDBusArgument &gen::enums::operator>>(const QDBusArgument &argument, Color::Type &object) {
    int tmp;
    argument >> tmp;
    object = static_cast<Color::Type>(tmp);
    return argument;
}